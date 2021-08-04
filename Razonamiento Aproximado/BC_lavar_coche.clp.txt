(deftemplate S
	0 6
	(
		(baja(0 1)(1 1)(3 0))
		(media(1 0)(3 1)(5 0))
		(alta(3 0)(5 1)(6 1))
	)

)

(deftemplate T
	0 6
	(
		(poco(0 1)(1 1)(3 0))
		(medio(1 0)(3 1)(5 0))
		(alto(3 0)(5 1)(6 1))
	)

)

(deftemplate potencia
	0 10
	(
		(muy_poca(0 1)(1 1)(3 0))
		(poca(1 0)(3 1)(5 0))
		(media(3 0)(5 1)(7 0))
		(alta(5 0)(7 1)(9 0))
		(muy_alta(7 0)(9 1)(10 1))
	)

)

(defrule regla_1
	(S baja)
	(T poco)
=>
	(assert (potencia muy_poca))
)

(defrule regla_2
	(S baja)
	(T medio)
=>
	(assert (potencia poca))
)

(defrule regla_3
	(S media)
	(T poco)
=>
	(assert (potencia poca))
)

(defrule regla_4
	(S media)
	(T alto)
=>
	(assert (potencia media))
)

(defrule regla_5
	(S grande)
	(T alto)
=>
	(assert (potencia alta))
)