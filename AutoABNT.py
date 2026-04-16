import uno

def AplicarFormatacaoABNT(*args):
    doc = XSCRIPTCONTEXT.getDocument()
    
    # 1. Margens (3cm Superior/Esquerda, 2cm Inferior/Direita) [cite: 5, 6, 82]
    estilos_pagina = doc.getStyleFamilies().getByName("PageStyles")
    estilo_padrao_pag = estilos_pagina.getByName("Standard")
    estilo_padrao_pag.TopMargin = 3000
    estilo_padrao_pag.LeftMargin = 3000
    estilo_padrao_pag.RightMargin = 2000
    estilo_padrao_pag.BottomMargin = 2000
    
    # 2. Estilo de Parágrafo (Corpo do Texto) [cite: 8, 11, 14, 64]
    estilos_para = doc.getStyleFamilies().getByName("ParagraphStyles")
    corpo = estilos_para.getByName("Standard")
    
    corpo.CharFontName = "Arial" # [cite: 7, 88]
    corpo.CharHeight = 12 # [cite: 8, 88]
    
    # Alinhamento Justificado (Valor 2 corresponde a JUSTIFIED) [cite: 13, 67, 89]
    corpo.ParaAdjust = 2 
    
    # Espaçamento 1,5 [cite: 11, 92]
    distancia = uno.createUnoStruct("com.sun.star.style.LineSpacing")
    distancia.Height = 150 
    corpo.ParaLineSpacing = distancia
    
    # Recuo 1,25cm [cite: 14, 64, 91]
    corpo.ParaFirstLineIndent = 1250 
    
    # 3. Estilo de Título (Sem recuo) [cite: 71, 94, 99]
    if estilos_para.hasByName("Heading 1"):
        titulo1 = estilos_para.getByName("Heading 1")
        titulo1.ParaFirstLineIndent = 0 # [cite: 99]
        titulo1.CharWeight = 150 # Negrito [cite: 98]
        titulo1.CharColor = 0 # Preto [cite: 98]
    
    return None
