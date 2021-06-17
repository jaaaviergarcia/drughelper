
  requireNamespace("readr")
  dhdrugs <- read_delim("https://raw.githubusercontent.com/jaaaviergarcia/drughelper/main/dhdrugs.tsv",
                            "\t", escape_double = FALSE, trim_ws = TRUE)

  load("../../data/input/2020-12-17version/singleDrugSynonymsChembl.RData")

  for (i in 1:nrow(dhdrugs)){
    dhdrugs$synonyms[i] <- toupper(dhdrugs$synonyms[i])
  }

  dhdrugs$synonymsChembl <- singleDrugSynonymsChembl$Drug_synonyms


  for (j in 1:nrow(dhdrugs)){
    if (is.na(dhdrugs$synonyms[j]))
      dhdrugs$synonyms[j] <- dhdrugs$synonymsChembl[j]
    else
      dhdrugs$synonyms[j] <- paste(dhdrugs$synonymsChembl[j], dhdrugs$synonyms[j], sep=";;;")
  }

  dhdrugs <- dhdrugs[,-7]

  #UNIQUE SYNONYMS
  #vaux = vector auxiliar
  for (k in 1:nrow(dhdrugs)){

    vaux <- strsplit(dhdrugs$synonyms[k], ";;;")[[1]]
    vaux <- unique(vaux)
    dhdrugs$synonyms[k] <- paste(vaux, collapse = ";;;")

  }



  source("../../codeJG/generateDB/formattingSynonymsTable.R")
  dhdrugs <- updateTable(dhdrugs)

  #Introducimos otras columnas como ids u otra información:

  dhdrugs$DrugHelper <- paste0("DH0",1:nrow(dhdrugs))

  #Ordenamos las columnas

  dhdrugs <- subset(dhdrugs, select = c(8,2,1,4,5,6,7,3))

  save(dhdrugs, file = "https://github.com/jaaaviergarcia/drughelper/dhdrugs.RData")



