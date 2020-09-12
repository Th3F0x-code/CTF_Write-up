# buildroot config
Change this line to your myconfig path.
```
BR2_LINUX_KERNEL_CUSTOM_CONFIG_FILE="/path/to/myconfig"
```
`myconfig` is for enabling userfaultfd system call. (in case some players use it for exploit)
```
CONFIG_USERFAULTFD=y
```
