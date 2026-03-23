const TASKS = {
  "urgente": [
    {
      "text": "Ángelito: mover presentación SpotLight (PPT de Ani) al canal de San Pablo — no a Herramientas y Utilidades. Coordinar por hilo interno antes de presentar al cliente",
      "account": "General",
      "project": "Agente IA UCSP",
      "tag": "Agente IA UCSP",
      "tagClass": "tag-def",
      "owner": "Ángelito",
      "clients": [],
      "isNew": true
    },
    {
      "text": "Enrique: esperar brief de César Puma para Mesa de Ayuda (integración IA + WhatsApp sobre Zoho) — propuesta para abril/mayo",
      "account": "UCSP",
      "project": "Mesa de Ayuda",
      "tag": "Mesa de Ayuda",
      "tagClass": "tag-uc",
      "owner": "Enrique",
      "clients": [
        "UCSP"
      ],
      "isNew": true
    },
    {
      "text": "Enrique: actualizar propuesta de coaching para equipo SGA de UCSP (ahora son 5-6 personas) y reenviar con alcance revisado",
      "account": "UCSP",
      "project": "General",
      "tag": "UCSP",
      "tagClass": "tag-uc",
      "owner": "Enrique",
      "clients": [
        "UCSP"
      ],
      "isNew": true
    },
    {
      "text": "Atender reunión urgente World Vision Perú — hoy 3pm | Preparar agenda: limpieza de listas + consulta web",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ángelito + Cristian P",
      "clients": [
        "WV"
      ]
    },
    {
      "text": "Ángelito: hacer push a Luis para activar campañas Wash esta semana (Día del Agua)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ángelito",
      "clients": [
        "WV"
      ]
    },
    {
      "text": "Cristian P: cerrar ticket donaciones únicas (ajuste en integración) — HOY",
      "account": "VP",
      "project": "General",
      "tag": "VP",
      "tagClass": "tag-vp",
      "owner": "Cristian P",
      "clients": [
        "VP"
      ]
    },
    {
      "text": "Cristian P: cerrar ticket limpieza negocios duplicados F2F (750 contactos) — HOY",
      "account": "VP",
      "project": "General",
      "tag": "VP",
      "tagClass": "tag-vp",
      "owner": "Cristian P",
      "clients": [
        "VP"
      ]
    },
    {
      "text": "Cristian P: escribir a María (WV PE) por Discord para obtener más info del ticket \"limpieza de lista y consulta web\"",
      "account": "VP",
      "project": "General",
      "tag": "VP",
      "tagClass": "tag-vp",
      "owner": "Cristian P",
      "clients": [
        "VP"
      ]
    },
    {
      "text": "Sofi: subir base de Iglesias — Esther confirmó que Jorge y ella tienen el trabajo listo. Pendiente ejecución.",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Sofía",
      "clients": [
        "WV"
      ]
    }
  ],
  "semana": [
    {
      "text": "Cristian P**",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Cristian",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Reenviar a Diana y equipo la lista y recursos para la importación de negocios pendientes (03:06)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Diana",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Compartir lista con 47 contactos con negocios duplicados para verificación interna (15:57)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ángelito",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Compartir workflow de reintento Face to Face para entender la lógica de asociar pagos a negocios correctos (15:45)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ángelito",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Proveer informe o lista de pagos únicos de donación para validación y creación correcta de negocios (19:32)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ángelito",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Ornella Baldi**",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ornella",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Revisar archivo y datos de nóminas subidos a Discord para validar con cifras propias (17:39)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ángelito",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Finalizar facturación mensual para agencias Face to Face y notificar a Pablo para coordinar análisis con sistema automático (38:03)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Pablo",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Comunicaciones Blue Nose**",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Ángelito",
      "clients": [],
      "isNew": true
    },
    {
      "text": "Generar un token de acceso personal en GitHub con permisos de repositorio y sin expiración para Fireflies (03:54)",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Ángelito",
      "clients": [],
      "isNew": true
    },
    {
      "text": "Configurar el webhook en GitHub con la URL proporcionada para notificaciones entre Fireflies y GitHub (06:06)",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Ángelito",
      "clients": [],
      "isNew": true
    },
    {
      "text": "Revisar la sección 'Actions' en GitHub para verificar que el workflow se ejecute correctamente después de cada reunión (10:32)",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Ángelito",
      "clients": [],
      "isNew": true
    },
    {
      "text": "Usar Fireflies para capturar reuniones en vivo introduciendo el enlace en la función 'Capture add to Live Meeting' (13:09)",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Ángelito",
      "clients": [],
      "isNew": true
    },
    {
      "text": "Pablo Perez**",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Pablo",
      "clients": [],
      "isNew": true
    },
    {
      "text": "Ayudar a Comunicaciones Blue Nose a entender cómo configurar el webhook correctamente y la función del header y body en las peticiones (07:41)",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Ángelito",
      "clients": [],
      "isNew": true
    },
    {
      "text": "Enrique: responder a César Puma para fijar reunión con equipo operativo (Ángela González, Rudy Hasawi, Juan Daniel Rodríguez) — resolver preguntas del correo de Pablo sobre Agente IA",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Enrique",
      "clients": [],
      "isNew": true
    },
    {
      "text": "Ángelito: hacer seguimiento a reunión con equipo operativo UCSP (Agente IA) — anotaciones de Enrique sobre matrícula, tienda virtual, facturación en el canal",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Ángelito",
      "clients": [],
      "isNew": true
    },
    {
      "text": "Cristian P: instalar MCPs de HubSpot, Cloudpod y GitHub en Antigravity (extensiones a la izquierda) — eliminar skills problemáticos, reinstalar solo los MCP necesarios",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Cristian P",
      "clients": [],
      "isNew": true
    },
    {
      "text": "Comunicaciones Blue Nose**",
      "account": "Smartimper",
      "project": "General",
      "tag": "Smartimper",
      "tagClass": "tag-sm",
      "owner": "Ángelito",
      "clients": [
        "Smartimper"
      ],
      "isNew": true
    },
    {
      "text": "Enrique: esperar brief de César Puma para propuesta Mesa de Ayuda (IA + WhatsApp sobre Zoho) — plazo: abril/mayo. Pablo confirmó que no hay problema de plataforma",
      "account": "UCSP",
      "project": "Mesa de Ayuda",
      "tag": "Mesa de Ayuda",
      "tagClass": "tag-uc",
      "owner": "Enrique",
      "clients": [
        "UCSP"
      ],
      "isNew": true
    },
    {
      "text": "Enrique: actualizar propuesta de coaching para equipo SGA (ahora 5-6 personas) y enviar con alcance revisado. César dejó de trabajar con Dzine Lab, buscan suplirlos",
      "account": "UCSP",
      "project": "Coaching SGA",
      "tag": "Coaching SGA",
      "tagClass": "tag-uc",
      "owner": "Enrique",
      "clients": [
        "UCSP"
      ],
      "isNew": true
    },
    {
      "text": "Enrique: hacer seguimiento a Efraín Centeno (Rector Académico) quien lidera comisión de alumni — ver si se activa el proyecto",
      "account": "UCSP",
      "project": "Alumni",
      "tag": "Alumni",
      "tagClass": "tag-uc",
      "owner": "Enrique",
      "clients": [
        "UCSP"
      ],
      "isNew": true
    },
    {
      "text": "Ángelito: mover presentación SpotLight de Ani al canal de San Pablo (no en Herramientas y Utilidades) · Coordinar reunión interna antes de presentar al cliente",
      "account": "UCSP",
      "project": "SpotLight PPT",
      "tag": "SpotLight PPT",
      "tagClass": "tag-uc",
      "owner": "Ángelito",
      "clients": [
        "UCSP"
      ],
      "isNew": true
    },
    {
      "text": "Ángelito: crear checklist unificado con IA de todos los puntos tratados en reuniones UCSP (1ra, 2da... 5ta) para blindar seguimiento de entregables y evitar pedidos de última hora",
      "account": "UCSP",
      "project": "General",
      "tag": "UCSP",
      "tagClass": "tag-uc",
      "owner": "Ángelito — usar transcripciones + Claude",
      "clients": [
        "UCSP"
      ],
      "isNew": true
    },
    {
      "text": "CENDES: María Daniela confirmó revisión en proceso (13.03) — cotización previa anulada. Esperar aprobación formal",
      "account": "UCSP",
      "project": "⚠️ EN PROCESO",
      "tag": "⚠️ EN PROCESO",
      "tagClass": "tag-uc",
      "owner": "Ángelito",
      "clients": [
        "UCSP"
      ]
    },
    {
      "text": "Enrique: coordinar entrevista con Ángelo sobre Centro de Idiomas + entrevistas con alumnos, desertores y estudiantes de otras universidades",
      "account": "UCSP",
      "project": "General",
      "tag": "UCSP",
      "tagClass": "tag-uc",
      "owner": "Enrique",
      "clients": [
        "UCSP"
      ]
    },
    {
      "text": "Enrique: esperar respuesta de Renzo sobre presupuesto adicional (cual + cuanti) para Centro de Idiomas — todo supeditado a esto",
      "account": "UCSP",
      "project": "General",
      "tag": "UCSP",
      "tagClass": "tag-uc",
      "owner": "Enrique",
      "clients": [
        "UCSP"
      ]
    },
    {
      "text": "Enrique: buscar espacio fortuito con Paul para preguntar por TDR Cobranzas (parar la mano por ahora)",
      "account": "UCSP",
      "project": "General",
      "tag": "UCSP",
      "tagClass": "tag-uc",
      "owner": "Enrique",
      "clients": [
        "UCSP"
      ]
    },
    {
      "text": "Enrique: tener espacio con Argenis (WV RD) para asegurar continuidad",
      "account": "UCSP",
      "project": "General",
      "tag": "UCSP",
      "tagClass": "tag-uc",
      "owner": "Enrique + Pablo",
      "clients": [
        "UCSP"
      ]
    },
    {
      "text": "Ángelito: soporte continúa · Se respondió inquietud sobre landing (sí la hacemos con el proceso de Trello) · Confirmar que todo fluye correctamente con el cliente",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ángelito",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Ángelito: reunión con Luis cancelada — reprogramada al próximo lunes. Seguir metiéndole presión para revisar contenidos",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ángelito",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Luis: hablar con Jorge Girón para conectar WhatsApp a cuenta de Meta",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Luis",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Express Pago: recibió primera documentación para conectar a web + HubSpot — están en espera. Cristian y Ángelito en lista de correos para seguimiento",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Cristian P + Ángelito",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Accionables canal: sincronizar campo \"nombre de iglesia\" en objeto Contactos · Investigar URL versión web · Cruzar video · Sincronizar campos PartnerID · Investigar integración leads con proveedores externos · NO usar módulo Operations · Sofía: confirmar si envió correo a Jorge",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Cristian P + Sofía",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Sofía: cruzar base SIMMA vs HubSpot junto a Jorge para identificar partners sin contacto ni pledge, emails provisionales sin actualizar, y campos faltantes",
      "account": "WV",
      "project": "SIMMA",
      "tag": "SIMMA",
      "tagClass": "tag-wv",
      "owner": "Sofía + Jorge",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Sofía: agendar reunión con Esther para revisar hallazgos y definir acciones correctivas sobre las 5 categorías (Partners, Email, Contacts, Phone, Pledges)",
      "account": "WV",
      "project": "SIMMA",
      "tag": "SIMMA",
      "tagClass": "tag-wv",
      "owner": "Sofía",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Sofía/Cristian P: configurar propiedades personalizadas de llamadas en HubSpot (ChildID, AddDate, MediaType, datos bancarios) según hallazgos de Esther",
      "account": "WV",
      "project": "SIMMA",
      "tag": "SIMMA",
      "tagClass": "tag-wv",
      "owner": "Sofía + Cristian P",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Cristian P: revisar con Esther qué hacer con datos bancarios presentes en Pledges SIMMA (decisión de seguridad/privacidad)",
      "account": "WV",
      "project": "SIMMA",
      "tag": "SIMMA",
      "tagClass": "tag-wv",
      "owner": "Cristian P",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Sofía: subir base de Iglesias — confirmado por Esther que Jorge y ella ya tienen el trabajo listo",
      "account": "WV",
      "project": "SIMMA",
      "tag": "SIMMA",
      "tagClass": "tag-wv",
      "owner": "Sofía",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Ángelito: asegurarse de que soporte con Dominicana esté activo como con Chile/Perú/Ecuador — actividad en Discord",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ángelito",
      "clients": [
        "WV"
      ]
    },
    {
      "text": "Equipo: aprovechar última/s reuniones con Argenis para hablar de continuidad (Yomara, Juan Plata, Juan Miralcázar, Eli Kauri se van — solo queda Argenis)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Enrique + Pablo",
      "clients": [
        "WV"
      ]
    },
    {
      "text": "Luis: finalizar y enviar piezas campaña Wash HOY o mañana (vitales para evento del domingo)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Luis",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Luis: enviar correo formal a Jorge solicitando permisos para editar web y publicar landing pages — CC a Pablo",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Luis",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Pablo: gestionar y facilitar permisos de edición web/landing para Luis — contacto formal con Jorge",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Pablo",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Pablo: orientar a Luis para localizar plantillas WhatsApp en HubSpot + verificar conexión del número que termina en 5550",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Pablo",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Luis: confirmar a quién está asignado el número WhatsApp (termina en 5550) para conectar plantillas correctamente",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Luis",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Pablo: incluir a desarrolladores técnicos en correos para integración con pasarela Express Pago",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Pablo",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Ángelito: coordinar con Luis y Pablo reunión anticipada de revisión de piezas y workflows — MIÉRCOLES (no jueves)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ángelito · Luis envía invitación",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Pablo: apoyar a Ángelito con bot de Telegram en sesión de aprendizaje del VIERNES",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Pablo",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Acompañar evolución de piezas para iniciar creación y activación de WF",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ángelito",
      "clients": [
        "WV"
      ]
    },
    {
      "text": "Reunión seguimiento con Express Pago — reprogramada para JUEVES (avance pasarela de pago)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ángelito",
      "clients": [
        "WV"
      ]
    },
    {
      "text": "Cristian P: continuar revisión con desarrolladores para resolver prefijos SMS — revisar correo que Pablo reenvía",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Cristian P",
      "clients": [
        "WV"
      ]
    },
    {
      "text": "Revisar comentarios de Nieves en Discord (canal general, varias peticiones)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ángelito",
      "clients": [
        "WV"
      ]
    },
    {
      "text": "⭐ Servicio renovado por un año más. Certificaciones de donación (desarrollo de Pablo) se cobran aparte por única vez",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ángelito (informativo)",
      "clients": [
        "WV"
      ]
    },
    {
      "text": "Valeria: convocar reuniones martes 11am Ecuador",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Valeria",
      "clients": [
        "WV"
      ]
    },
    {
      "text": "Gonzalo: aprobar proyecto Facturación F2F + compartir reglas de negocio con Pablo",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Gonzalo / seguimiento Enrique",
      "clients": [
        "WV"
      ]
    },
    {
      "text": "Ángelito: analizar y documentar gestión del equipo de ventas UPSJB — de 11,000 leads contactados vía WhatsApp, 5,300 abrieron el mensaje, 325 respondieron y el 95% no recibió respuesta del equipo de ventas. Preparar punto para próxima reunión",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Ángelito → Pablo",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Equipo Blue Nose: revisar puntos resaltados en amarillo (oportunidades) y rojo (debilidades/riesgos) en los 3 documentos enviados por Enrique — definir acciones correctivas",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Ángelito + Enrique",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Ángelito: responder correo de Enrique confirmando revisión y coordinar fecha de presentación de acciones correctivas",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Ángelito",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Blue Nose: asignar equipo exclusivo para contactar 4,800 leads sin gestión (modalidad a distancia)",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Enrique/Pablo",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Blue Nose: implementar SLA ≤5 min de atención a leads + prohibir cierre por intento límite sin flujo de nutrición",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Blue Nose",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Blue Nose: desarrollar kit de confianza para padres (video infraestructura + validaciones institucionales + simulación ahorro vía WhatsApp)",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Blue Nose",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Blue Nose: elaborar argumentario para modalidad online (rigor académico, empleabilidad, testimonios)",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Blue Nose",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Blue Nose: evaluar implementación de tutores virtuales con IA para estudiantes a distancia",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Blue Nose",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Carlos: confirmar uso de sala B para reunión de lanzamiento",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Carlos",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Carlos: enviar lista oficial de modalidades especiales de admisión pendientes y cierre de postulaciones",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Carlos",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Carlos: finalizar limpieza de contactos duplicados y negocios en HubSpot",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Carlos",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Carlos: remitir a Blue Nose programas de Admón de Negocios Internacionales y Marketing actualizados",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Carlos",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Estuardo: completar y entregar Buyer Persona para padres esta semana",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Estuardo",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Estuardo: coordinar registro digital de asistencia en ferias de padres desde quincena de marzo",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Estuardo",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Estuardo: enviar estrategia de marketing individualizada por carrera",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Estuardo",
      "clients": [
        "UPSJB"
      ],
      "isNew": true
    },
    {
      "text": "Carlos: consultar avance de contacto a descalificados (100/día por asesor)",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Carlos",
      "clients": [
        "UPSJB"
      ]
    },
    {
      "text": "Carlos: solicitar entrega final MVP a Atom esta semana",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Carlos",
      "clients": [
        "UPSJB"
      ]
    },
    {
      "text": "Carlos: compartir nuevo estudio de mercado (Admón y Conta) con Blue Nose",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Carlos",
      "clients": [
        "UPSJB"
      ]
    },
    {
      "text": "Enrique: presentar análisis estratégico de modalidad A Distancia",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Enrique",
      "clients": [
        "UPSJB"
      ]
    },
    {
      "text": "Cristian P: crear y organizar tickets de Ecuador (mezcla HubSpot + integraciones + nuevas propuestas) — priorizar por urgencia, avanzar de a 2 en paralelo, NO sacar todos de golpe",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Cristian P + Pablo + Marcos",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Cristian P: hacer recordatorio a María (WV PE) por Discord — enviar listado de consultas sobre edición web/CMS (aún no las han enviado)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Cristian P",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Pablo + Marcos: avanzar clasificación de listas HubSpot Perú (700 listas) — identificar las que tienen leads vs otras · Ya hecho análisis inicial con IA; siguiente paso: clasificar con columna en Excel",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Pablo + Marcos",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Cristian P: reenviar a Diana lista y recursos para importación de negocios pendientes (faltan negocios asociados a contactos web que Pau importó)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Cristian P",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Cristian P: compartir lista de 47 contactos con negocios duplicados para verificación interna de Diana + Ornella",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Cristian P",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Cristian P: compartir workflow de reintento F2F para entender lógica de asociación de pagos a negocios correctos",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Cristian P",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Cristian P: proveer informe/lista de pagos únicos de donación para validación y creación correcta de negocios",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Cristian P",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Diana + Ornella: revisar lista de contactos y negocios importados — dar de baja negocios duplicados o incorrectos",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Diana + Ornella",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Ornella: revisar archivo de nóminas subido a Discord + finalizar facturación manual de agencias F2F (enero y febrero) — avisar a Pablo para coordinar",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Ornella",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Diana: mostrar a Gonzalo demo de gestión de niños apadrinados (integración Horizon) para evaluar implementación local",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Diana",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Pablo: presionar a Jorge para mejorar estructura del objeto niños en países desorganizados (Ecuador, Brasil)",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Pablo",
      "clients": [
        "WV"
      ],
      "isNew": true
    },
    {
      "text": "Compartir reporte de nóminas a Gonzalo, Diana y Ornella para validación",
      "account": "VP",
      "project": "NUEVO",
      "tag": "NUEVO",
      "tagClass": "tag-vp",
      "owner": "Cristian P",
      "clients": [
        "VP"
      ],
      "isNew": true
    },
    {
      "text": "Diani: enviar DB para importación de negocios (WF métodos de pago)",
      "account": "VP",
      "project": "General",
      "tag": "VP",
      "tagClass": "tag-vp",
      "owner": "Diani",
      "clients": [
        "VP"
      ]
    },
    {
      "text": "Esperar regreso de Ornella para avanzar proceso nóminas con SIMMA",
      "account": "VP",
      "project": "General",
      "tag": "VP",
      "tagClass": "tag-vp",
      "owner": "Equipo",
      "clients": [
        "VP"
      ]
    },
    {
      "text": "Pablo: avanzar con la parte de ventas de la financiera (no esperar a marketing)",
      "account": "General",
      "project": "FINANCIERA",
      "tag": "FINANCIERA",
      "tagClass": "tag-def",
      "owner": "Pablo",
      "clients": [],
      "isNew": true
    },
    {
      "text": "Pablo: Juan Camilo de Foxport enviará presupuesto de licencias — preparar presupuesto de acompañamiento",
      "account": "General",
      "project": "CONSTRUCTORA",
      "tag": "CONSTRUCTORA",
      "tagClass": "tag-def",
      "owner": "Pablo + Enrique",
      "clients": [],
      "isNew": true
    },
    {
      "text": "Valdric Tardos**",
      "account": "Smartimper",
      "project": "General",
      "tag": "Smartimper",
      "tagClass": "tag-sm",
      "owner": "Ángelito",
      "clients": [
        "Smartimper"
      ],
      "isNew": true
    },
    {
      "text": "Poder concretar la contratación de un VDR (representante virtual de ventas) que se encargue de la prospección y generación de reuniones para facilitar cierres de ventas (06:40)",
      "account": "Smartimper",
      "project": "General",
      "tag": "Smartimper",
      "tagClass": "tag-sm",
      "owner": "Ángelito",
      "clients": [
        "Smartimper"
      ],
      "isNew": true
    },
    {
      "text": "Una vez contratado el VDR, comunicar su incorporación para reiniciar el servicio y seguimiento con el equipo (10:30)",
      "account": "Smartimper",
      "project": "General",
      "tag": "Smartimper",
      "tagClass": "tag-sm",
      "owner": "Ángelito",
      "clients": [
        "Smartimper"
      ],
      "isNew": true
    },
    {
      "text": "Supervisar personalmente la fase actual de ventas mientras no se cuente con el nuevo recurso (06:40)",
      "account": "Smartimper",
      "project": "General",
      "tag": "Smartimper",
      "tagClass": "tag-sm",
      "owner": "Ángelito",
      "clients": [
        "Smartimper"
      ],
      "isNew": true
    },
    {
      "text": "Continuar con la coordinación y apoyo temporal en la planificación y organización del proyecto tras la salida de Anita (00:00)",
      "account": "Smartimper",
      "project": "General",
      "tag": "Smartimper",
      "tagClass": "tag-sm",
      "owner": "Ángelito",
      "clients": [
        "Smartimper"
      ],
      "isNew": true
    },
    {
      "text": "Mantener coordinación para asegurar la correcta entrega y configuración de materiales digitales, confirmando el estado actual de las landing pages y correos (13:50)",
      "account": "Smartimper",
      "project": "General",
      "tag": "Smartimper",
      "tagClass": "tag-sm",
      "owner": "Ángelito",
      "clients": [
        "Smartimper"
      ],
      "isNew": true
    },
    {
      "text": "Pablo Pérez**",
      "account": "Smartimper",
      "project": "General",
      "tag": "Smartimper",
      "tagClass": "tag-sm",
      "owner": "Pablo",
      "clients": [
        "Smartimper"
      ],
      "isNew": true
    },
    {
      "text": "Ángelito: escribirle al cliente cada 2-3 semanas para preguntar cómo va con la incorporación del BDR | Si no hay respuesta → avisar a Enrique para que entre él",
      "account": "Smartimper",
      "project": "NUEVO",
      "tag": "NUEVO",
      "tagClass": "tag-sm",
      "owner": "Ángelito",
      "clients": [
        "Smartimper"
      ],
      "isNew": true
    },
    {
      "text": "Enrique: avisar si hay alguna novedad para confirmar inicio del proyecto",
      "account": "Ica",
      "project": "General",
      "tag": "Ica",
      "tagClass": "tag-ci",
      "owner": "Enrique",
      "clients": [
        "Ica"
      ]
    }
  ],
  "mes": [
    {
      "text": "Presentar ideas en reunión de abril (ppt ya lista) | Due: primer miércoles de abril",
      "account": "UCSP",
      "project": "General",
      "tag": "UCSP",
      "tagClass": "tag-uc",
      "owner": "Equipo",
      "clients": [
        "UCSP"
      ]
    },
    {
      "text": "Gestionar cierre formal de contrato | Due: 31.03.26",
      "account": "WV",
      "project": "General",
      "tag": "WV",
      "tagClass": "tag-wv",
      "owner": "Equipo",
      "clients": [
        "WV"
      ]
    }
  ],
  "done": [
    {
      "text": "Enrique: responder a César Puma para fijar reunión con equipo operativo (Ángela González, Rudy Hasawi, Juan Daniel Rodríguez) y resolver todas las preguntas del correo de Pablo",
      "account": "General",
      "project": "Agente IA UCSP",
      "tag": "Agente IA UCSP",
      "tagClass": "tag-def",
      "owner": "Enrique",
      "clients": [],
      "isNew": true,
      "isCompleted": true
    },
    {
      "text": "Pablo: dar permisos a Marcos para envío a lista de 5,600 contactos Blue Nose (envíos en 3 bloques de ~2,000 por mes) — verificar número de contactos de marketing antes ✅ Permisos dados en reunión",
      "account": "UPSJB",
      "project": "General",
      "tag": "UPSJB",
      "tagClass": "tag-up",
      "owner": "Pablo",
      "clients": [
        "UPSJB"
      ],
      "isNew": true,
      "isCompleted": true
    },
    {
      "text": "Marcos: crear propiedad en HubSpot para segmentar lista Blue Nose (5,600 contactos) y dividir en 3 grupos para envíos de ~2,000 por mes · Permisos ya dados por Pablo ✅",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Marcos",
      "clients": [],
      "isNew": true,
      "isCompleted": true
    },
    {
      "text": "Enrique: documentos de análisis, diagnóstico y recomendaciones del Programa A Distancia enviados a UPSJB",
      "account": "General",
      "project": "✅  11:52",
      "tag": "✅  11:52",
      "tagClass": "tag-def",
      "owner": "Equipo",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "Smartimper: entregar todos los contenidos y producción en HubSpot",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Smartimper",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "Smartimper: entregar 2 landings con producción en HubSpot",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Smartimper",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "Smartimper: configurar propiedades de Contactos y Negocios",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Smartimper",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "Smartimper: reunión de continuidad realizada — servicio culminado (de momento) · Contexto: se trabajó diseño y contenido para todo el año en 1 mes transitorio bajo compromiso de renovación que no se honró. Renovación depende de que el cliente consiga su BDR.",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Smartimper",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "WV RD: entregar todo lo pendiente por parte del equipo",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "WV RD",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "UCSP CENDES: enviar correo al cliente sobre cotización sin efecto",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "UCSP CENDES",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "UCSP: Ani envió correo de seguimiento a Santiago (Experiencia al Estudiante)",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "UCSP",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "Ani: compartió presentación de SpotLight para revisión",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Ani",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "VP Chile: Marquitos entregó reporte de negocios duplicados F2F",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "VP Chile",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "VP Chile: subir nóminas Feb de Multibanca y Transdata ✅",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "VP Chile",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "WV HND: entregar piezas + landing pages",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "WV HND",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "WV ES: Esther respondió con revisión de base de datos (Jorge y ella lo tienen)",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "WV ES",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "WV ES: renovación de contrato cerrada — continúa por un año más",
      "account": "General",
      "project": "NUEVO ✅",
      "tag": "NUEVO ✅",
      "tagClass": "tag-def",
      "owner": "Equipo",
      "clients": [],
      "isNew": true,
      "isCompleted": true
    },
    {
      "text": "UCSP: Enrique le pasó presupuesto a Renzo para investigaciones adicionales (Centro de Idiomas)",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "UCSP",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "UCSP Agente IA: Alonso respondió — derivó preguntas a César Puma",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "UCSP Agente IA",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "World Vision Brasil — sin novedad",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Equipo",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "Costa Rica — CANCELADO",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Equipo",
      "clients": [],
      "isCompleted": true
    },
    {
      "text": "UCSP Cobranzas TDR — Enrique para la mano; espera cruce con Paul",
      "account": "General",
      "project": "General",
      "tag": "General",
      "tagClass": "tag-def",
      "owner": "Equipo",
      "clients": [],
      "isCompleted": true
    }
  ]
};
