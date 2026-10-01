;; =========================================================
;; 1. PLANTILLAS Y CONTROL DE FLUJO
;; =========================================================

(deftemplate paciente
   (slot estado (type SYMBOL))
   (slot dosis-menor-igual-75 (type SYMBOL))   ; si / no
   (slot condicion-debil (type SYMBOL))        ; si / no
   (slot resultado (type SYMBOL))              ; Curacion / Defuncion
)

(deftemplate fase
   (slot actual (type SYMBOL))                 ; inicio, preguntar-dosis, preguntar-condicion, final
)

;; =========================================================
;; 2. INICIO: PREGUNTA EL ESTADO DE LA ENFERMEDAD
;; =========================================================

(deffacts inicio
   (fase (actual inicio))
   (paciente)
)

(defrule preguntar-estado
   ?f <- (fase (actual inicio))
   ?p <- (paciente)
   =>
   (printout t crlf "=== DIAGNOSTICO CLINICO ===" crlf)
   (printout t "Cual es el estado de la enfermedad? (Incipiente / Avanzado / Terminal): ")
   (bind ?resp (read))
   (modify ?p (estado ?resp))
   
   ;; Derivacion segun el estado ingresado
   (if (eq ?resp Incipiente)
      then (modify ?f (actual preguntar-dosis))
      else 
         (if (eq ?resp Avanzado)
            then 
               (modify ?p (resultado Curacion))
               (modify ?f (actual final))
            else
               (if (eq ?resp Terminal)
                  then (modify ?f (actual preguntar-condicion))
                  else
                     (printout t "Estado no valido. Por favor reinicie e intente de nuevo." crlf)
                     (modify ?f (actual final))
               )
         )
   )
)

;; =========================================================
;; 3. RAMA INCIPIENTE: EVALUACION DE DOSIS
;; =========================================================

(defrule preguntar-dosis
   ?f <- (fase (actual preguntar-dosis))
   ?p <- (paciente (estado Incipiente))
   =>
   (printout t "El numero de dosis es menor o igual a 75? (si / no): ")
   (bind ?resp (read))
   (modify ?p (dosis-menor-igual-75 ?resp))
   
   (if (eq ?resp si)
      then (modify ?p (resultado Curacion))
      else (modify ?p (resultado Defuncion))
   )
   (modify ?f (actual final))
)

;; =========================================================
;; 4. RAMA TERMINAL: EVALUACION DE CONDICION FISICA
;; =========================================================

(defrule preguntar-condicion
   ?f <- (fase (actual preguntar-condicion))
   ?p <- (paciente (estado Terminal))
   =>
   (printout t "Tiene condicion fisica debil? (si / no): ")
   (bind ?resp (read))
   (modify ?p (condicion-debil ?resp))
   
   (if (eq ?resp si)
      then (modify ?p (resultado Curacion))
      else (modify ?p (resultado Defuncion))
   )
   (modify ?f (actual final))
)

;; =========================================================
;; 5. CONCLUSION: MUESTRA EL EFECTO FINAL
;; =========================================================

(defrule mostrar-resultado
   (fase (actual final))
   (paciente (resultado ?res&~nil))
   =>
   (printout t crlf "--------------------------------" crlf)
   (printout t "EFECTO FINAL: " ?res crlf)
   (printout t "--------------------------------" crlf)
)
