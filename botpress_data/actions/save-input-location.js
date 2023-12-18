  /**
   * Read and store input locaiton
   * @title read and store input location
   * @category CustomSotrage
   * @author Ahmad
   * @param {string} inputLocation - InputLocation

   */
  const myAction = async inputLocation => {
    if (inputLocation === null || inputLocation === '') {
      bp.logger.warn(`Input Location is: ${inputLocation}`)
      return
    }
    bp.logger.info(`Setting session.locationData.inputLocation to: ${inputLocation}`)
    bp.logger.info(`Setting session.locationData.location to: ${inputLocation}`)
    event.state.session.locationData.inputLocation = inputLocation
    event.state.session.locationData.location = inputLocation
  }

  return myAction(args.inputLocation)
