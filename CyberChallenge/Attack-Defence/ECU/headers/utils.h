#include <stdint.h>
#include <libpq-fe.h>

#define DBPGconn "dbname = ecu_db"

/*
 * A function is marked as SAFE if it does not contain (intended) vulnerabilities.
 * Otherwise, it may be exploitable, or may be not... :)
 * __attribute__ specifiers can be safely ignored.
 */

void remove_new_line(char *buff);                                 /* SAFE */
uint8_t delete_old_entry();                                       /* SAFE */
void db_exit_with_message(PGconn *db);                            /* SAFE */
uint8_t add_message_to_db(uint64_t id, char *message, char *key); /* SAFE */
void print_all_messages();                                        /* SAFE */
uint8_t check_memory_key(uint64_t id, char *key);                 /* SAFE */
void print_memory(uint64_t id);                                   /* SAFE */
void update_message_db(uint64_t id, char *message);               /* SAFE */
uint8_t id_available(uint64_t id);                                /* SAFE */
void list_ids();                                                  /* SAFE */
uint8_t strtoull_wrap(char *buff, unsigned long long int *res);   /* SAFE */