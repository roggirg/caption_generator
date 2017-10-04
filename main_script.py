import caption_generator.prepare_dataset as prep_data

c_train, c_test = prep_data.prepare_dataset()
print "Training samples = " + str(c_train)
print "Test samples = " + str(c_test)
