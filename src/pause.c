/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   pause.c	:+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ntrancha <ntrancha@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2015/04/14 01:55:09 by ntrancha          #+#    #+#             */
/*   Updated: 2015/04/14 01:55:09 by ntrancha         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <time.h>
#include <stdio.h>

void          mon_sleep(double nbresec)
{
    clock_t   goal;
    goal = (nbresec * CLOCKS_PER_SEC / 100) + clock();
    while(goal > clock())
    {
        ; // en attendant l'heure cible ... on ne fait rien du tout !
    }
}

int			main(int argc, char **argv)
{
	mon_sleep(atoi(argv[1]));
	return (1);
}
