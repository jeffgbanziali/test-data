/*1 Selection des joueurs basés sur leur attribut */
SELECT
    *
FROM
    Joueurs j
    JOIN Attributs a1 ON j.attribut1_id = a1.id
    JOIN Attributs a2 ON j.attribut2_id = a2.id
WHERE
    a1.nom = 'vitesse'
    AND a1.description = 'élevé'
    AND a2.nom = 'agilité'
    AND a2.description = 'excellent';

/*************************************************************************************************************************************************************************************************/
/*2 Créetion d'une Vue pour les Détails des Joueurs  */


CREATE VIEW DétailsJoueurs AS
SELECT
    j.id,
    j.nom,
    p.nom AS position,
    a1.nom AS attribut1_nom,
    a1.description AS attribut1_description,
    a2.nom AS attribut2_nom,
    a2.description AS attribut2_description
FROM
    Joueurs j
    JOIN Positions p ON j.position_id = p.id
    JOIN Attributs a1 ON j.attribut1_id = a1.id
    JOIN Attributs a2 ON j.attribut2_id = a2.id;

/************************************************************************************************************************************************************/


/*3 les Joueurs correspondant à des critères spécifiques selon :.
 3. a.  les joueurs adaptés à la position d'Attaquant :*/


SELECT
    *
FROM
    Joueurs j
    JOIN Positions p ON j.position_id = p.id
WHERE
    p.nom = 'Attaquant';

/*************************************************************************************************************************************************************************************************/
/*3.b. les joueurs polyvalents :*/
SELECT
    *
FROM
    Joueurs j
    JOIN Attributs a ON j.attribut1_id = a.id
    OR j.attribut2_id = a.id
WHERE
    a.description IN ('vitesse', 'précision', 'endurance')
GROUP BY
    j.id
HAVING
    COUNT(DISTINCT a.id) >= 3;

/************************************************************************************************************************************************************/
/*4. Approche pour construire une requête permettant d’optimiser le Processus de Sélection de Joueurs :*/
/*Une approche pour optimiser le processus de sélection de joueurs pourrait être de créer des vues ou 
 des procédures stockées qui pré - filtrent les joueurs en fonction de critères spécifiques définis par le coach,
 tels que les attributs requis pour chaque position ou les attributs polyvalents pour certains rôles.*/
/****Pré-filtrage des joueurs basé sur les attributs et les positions**/
SELECT
    j.id,
    j.nom,
    p.nom AS position,
    a1.nom AS attribut1_nom,
    a1.description AS attribut1_description,
    a2.nom AS attribut2_nom,
    a2.description AS attribut2_description
FROM
    Joueurs j
    JOIN Positions p ON j.position_id = p.id
    JOIN Attributs a1 ON j.attribut1_id = a1.id
    JOIN Attributs a2 ON j.attribut2_id = a2.id
WHERE
    (
        a1.nom = 'vitesse'
        AND a1.description = 'élevé'
    )
    AND (
        a2.nom = 'agilité'
        AND a2.description = 'excellent'
    )
    AND (p.nom = 'Attaquant');

/*------------------------------------------------------------------------------------------------------------*/
/*** Calcul des performances globales des joueurs**/



SELECT
    j.nom AS joueur,
    COUNT(
        CASE
            WHEN am.action_type = 'but' THEN 1
        END
    ) AS buts_marques,
    COUNT(
        CASE
            WHEN am.action_type = 'tacle' THEN 1
        END
    ) AS tacles_reussis,
    COUNT(
        CASE
            WHEN am.action_type = 'passe décisive' THEN 1
        END
    ) AS passes_decisives
FROM
    Joueurs j
    JOIN ActionsMatchs am ON j.id = am.joueur_id
GROUP BY
    j.nom;

/*------------------------------------------------------------------------------------------------------------------------------------*/
/*** Analyse comparative***/



SELECT
    j.nom AS joueur,
    (
        SELECT
            COUNT(*)
        FROM
            ActionsMatchs am
        WHERE
            am.joueur_id = j.id
    ) AS nombre_actions
FROM
    Joueurs j
ORDER BY
    nombre_actions DESC;

/*******************************************************************************************************v****************/



/*Partie Bonus
 5. Analyse Avancée des Statistiques des Joueurs : :*/


SELECT
    j.nom AS joueur,
    COUNT(
        CASE
            WHEN am.action_type = 'but' THEN 1
        END
    ) AS buts_marques,
    COUNT(
        CASE
            WHEN am.action_type = 'tacle' THEN 1
        END
    ) AS tacles_reussis,
    COUNT(
        CASE
            WHEN am.action_type = 'passe décisive' THEN 1
        END
    ) AS passes_decisives,
    COUNT(*) AS actions_totales,
    ROUND(
        (
            COUNT(
                CASE
                    WHEN am.action_type = 'but' THEN 1
                END
            ) / NULLIF(COUNT(*), 0)
        ) * 100,
        2
    ) AS taux_conversion_buts,
    ROUND(
        (
            COUNT(
                CASE
                    WHEN am.action_type = 'tacle' THEN 1
                END
            ) / NULLIF(COUNT(*), 0)
        ) * 100,
        2
    ) AS taux_reussite_tacles,
    ROUND(
        (
            COUNT(
                CASE
                    WHEN am.action_type = 'passe décisive' THEN 1
                END
            ) / NULLIF(COUNT(*), 0)
        ) * 100,
        2
    ) AS taux_reussite_passes_decisives
FROM
    Joueurs j
    JOIN ActionsMatchs am ON j.id = am.joueur_id
GROUP BY
    j.nom;

/************************************************************************************************************************************************************/