SELECT * FROM levelupapi_event

SELECT
  g.id,
  g.user_id,
  e.description,
  e.date,
  e.time,
  e.game_id,
  e.organizer_id,
  u.id,
  u.first_name,
  u.last_name
FROM
  levelupapi_gamer g
JOIN
  levelupapi_gamer_sign_up_events su ON su.gamer_id = g.id
JOIN
  levelupapi_event e ON su.event_id = e.id
JOIN 
  auth_user u ON g.user_id = u.id