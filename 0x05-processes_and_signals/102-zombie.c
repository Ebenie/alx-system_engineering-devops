#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void) {
    int i;
    for (i = 0; i < 5; i++) {
        pid_t pid = fork();
        if (pid > 0) {
            printf("Zombie process created, PID: %d\n", pid);
            sleep(1);
        } else {
            exit(0);
        }
    }
    infinite_while();
    return 0;
}

int infinite_while(void) {
    while (1) {
        sleep(1);
    }
    return 0;
}
