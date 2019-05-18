/* Gustavo Martins Collaco 111851
 * Tamires Beatriz da Silva Lucena 111866
 *
 * Function prototypes.
 */

struct schedproc;

/* main.c */
int main(void);
void setreply(int proc_nr, int result);

/* schedule.c */
int rando(void); /* MODIFICADO: funcao para implementar o random */
struct schedproc *lottery(void); /* MODIFICADO: funcao que realiza o sorteio do processo */
int do_noquantum(message *m_ptr);
int do_start_scheduling(message *m_ptr);
int do_stop_scheduling(message *m_ptr);
int do_nice(message *m_ptr);
void init_scheduling(void);
void balance_queues(void);

/* utility.c */
int no_sys(int who_e, int call_nr);
int sched_isokendpt(int ep, int *proc);
int sched_isemtyendpt(int ep, int *proc);
int accept_message(message *m_ptr);
