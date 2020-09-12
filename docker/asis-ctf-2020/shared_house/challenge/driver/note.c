#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/cdev.h>
#include <linux/fs.h>
#include <linux/uaccess.h>
#include <linux/slab.h>
#include <linux/ioctl.h>
#include <linux/mutex.h>
#include "note.h"

static int __init module_initialize(void);
static void __exit module_cleanup(void);
static long mod_ioctl(struct file*, unsigned int, unsigned long);

static dev_t dev_id;
static struct cdev c_dev;
static struct file_operations module_fops = {
  .owner = THIS_MODULE,
  .unlocked_ioctl = mod_ioctl,
};

struct mutex __mutex;
int size = 0;
char *note = NULL;

static long mod_ioctl(struct file *filp, unsigned int cmd, unsigned long _arg)
{
  Command arg;
  if (copy_from_user(&arg, (void*)_arg, sizeof(Command))) return -EFAULT;
  if (arg.size < 0 || arg.size > MAX_NOTE_SIZE) return -EINVAL;

  mutex_lock(&__mutex);

  switch(cmd) {
  case CMD_ALLOC:
    if (note) kfree(note);
    size = arg.size;
    note = kzalloc(arg.size, GFP_KERNEL);
    if (note == NULL) goto ioctl_fail;
    break;
  case CMD_DELETE:
    if (note == NULL) goto ioctl_fail;
    kfree(note);
    note = NULL;
    break;
  case CMD_STORE:
    if (note == NULL) goto ioctl_fail;
    if (arg.size > size) goto ioctl_fail;
    if (copy_from_user(note, arg.note, arg.size)) goto ioctl_fail;
    note[arg.size] = 0;
    break;
  case CMD_LOAD:
    if (note == NULL) goto ioctl_fail;
    if (arg.size > size) goto ioctl_fail;
    if (copy_to_user(arg.note, note, arg.size)) goto ioctl_fail;
    break;
  default:
    goto ioctl_fail;
  }

  mutex_unlock(&__mutex);
  return 0;

 ioctl_fail:
  mutex_unlock(&__mutex);
  return -EINVAL;
}

static int __init module_initialize(void)
{
  if (alloc_chrdev_region(&dev_id, 0, 1, DEVICE_NAME)) {
    printk(KERN_WARNING "note: Failed to register device\n");
    return -EBUSY;
  }

  cdev_init(&c_dev, &module_fops);
  c_dev.owner = THIS_MODULE;

  if (cdev_add(&c_dev, dev_id, 1)) {
    printk(KERN_WARNING "note: Failed to add cdev\n");
    unregister_chrdev_region(dev_id, 1);
    return -EBUSY;
  }

  mutex_init(&__mutex);

  return 0;
}

static void __exit module_cleanup(void)
{
  cdev_del(&c_dev);
  unregister_chrdev_region(dev_id, 1);
}

module_init(module_initialize);
module_exit(module_cleanup);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("ptr-yudai");
MODULE_DESCRIPTION("ASIS CTF Quals 2020");
