from bunch import Bunch


config = {
    'NUM_EPOCHS': 4,    
    "BATCH_SIZE": 1,
    "BUFFER_SIZE": 1000,
    "INITIAL_LR": 0.003,
    "WARMUP_STEPS": 4000,
    "SEQ_LEN": 512,
    "MAX_EXAMPLE_LEN": 512,
    "VOCAB_SIZE": 30522,    
    "NUM_LAYERS": 8,
    "D_MODEL": 768,
    "D_FF": 2048,    
    "NUM_HEADS": 8,
    "DROPOUT_RATE": 0.1,
    "LOGDIR": 'log',
    "CHECKPOINTDIR": 'checkpoint'
}

config = Bunch(config)


