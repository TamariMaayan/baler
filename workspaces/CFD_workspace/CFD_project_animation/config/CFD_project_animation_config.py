def set_config(c):
    c.input_path = "workspaces/CFD_workspace/data/CFD_animation.npz"
    c.compression_ratio = 5
    #c.number_of_columns = 25
    #c.latent_space_size = 5
    c.epochs = 2000
    c.early_stopping = False
    c.early_stopping_patience = 100
    c.min_delta = 0
    c.lr_scheduler = True
    c.lr_scheduler_patience = 50
    c.model_name = "FPGA_DNNPorotypeAutoencoder"#"CFD_dense_AE"
    c.model_type = "dense"
    c.custom_norm = True
    c.l1 = True
    c.reg_param = 0.001
    c.RHO = 0.05
    c.lr = 0.001
    c.batch_size = 6000
    c.test_size = 0
    c.data_dimension = 2
    c.apply_normalization = False
    c.extra_compression = False
    c.intermittent_model_saving = False
    c.intermittent_saving_patience = 100
    c.activation_extraction = False
    c.deterministic_algorithm = False
    c.compress_to_latent_space = False
    c.save_error_bounded_deltas = False
    c.error_bounded_requirement = 1
    c.convert_to_blocks = [1,1,25]
    # c.custom_loss_function = "loss_function_swae"

    c.separate_model_saving = False


# == hls4ml configuration options ==

    c.hls4ml_model_name            = "FPGA_DNNPorotypeEncoder"
    c.default_reuse_factor         = 25
    c.default_precision            = "ap_fixed<16,8>"
    c.Strategy                     = "resource"
    c.Part                         = "xczu7ev-ffvc1156-2-e"
    c.ClockPeriod                  = 3
    c.IOType                       = "io_stream" 
    c.InputShape                   = (1,25)
    c.ProjectName                  = "r1_ios"
    c.OutputDir                    = "workspaces/CFD_workspace/rr1_ios/output/hls4ml"
    c.InputData                    = None
    c.OutputPredictions            = None
    c.csim                         = False
    c.synth                        = True
    c.cosim                        = False
    c.export                       = False


#     c.mse_sum = True
#     c.emd = False
#     c.l1 = True
#     c.activation_extraction = False
#     c.deterministic_algorithm = False
