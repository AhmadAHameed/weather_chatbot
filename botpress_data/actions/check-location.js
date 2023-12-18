  /**
   * Check Location Validity
   * @title LocationValidityChecker
   * @category Checkers
   * @author Ahmad
   */

  // Check copying this configuration to the shared.js file
  // Be careful as I had some troubles doing this with the traditional way
  event.state.session.locationData = {
    extractedLocation: '',
    locationTypo: false,
    inputLocation: '',
    nearestLocation: '',
    location: ''
  }
  // event.state.session.locationData = weatherLocationStructure
  bp.logger.info(`Setting session.locationData to:\t${JSON.stringify(event.state.session.locationData)}`)

  const locationValidityChecker = async () => {
    try {
      const location = await getLocationValue(event.state.session.entities)
      bp.logger.info(`found location: "${location}", found location type: "${typeof location}"`)
      if (location !== undefined && location !== null) {
        event.state.session.locationData.extractedLocation = location
        event.state.session.locationData.location = location
        bp.logger.info(
          `Setting session.locationData.extractedLocation to:\t ${event.state.session.locationData.extractedLocation}`
        )
      } else {
        bp.logger.info('Location value is undefined or null')
        event.state.session.locationData.location = ''
      }
    } catch (error) {
      bp.logger.error(error)
    }
  }

  const getLocationValue = async entityList => {
    const locationEntity = entityList.find(entity => entity.entity === 'location')
    return locationEntity ? locationEntity.value : null
  }

  return locationValidityChecker()
