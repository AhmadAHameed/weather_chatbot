const axios = require('axios')
const { host } = require('./shared')
/**
 * Requesting realtime weather info
 * @title GetRealtimeWeatherInfo
 * @category APIs
 * @author Ahmad
 * @param {string} inputLocation - Location to get realtime weather for
 */
const requestRealtimeWeather = async inputLocation => {
  try {
    bp.logger.info(`Input location for request is: ${JSON.stringify(inputLocation)}`)
    const data = JSON.stringify({ location: inputLocation })
    const config = {
      method: 'post',
      maxBodyLength: Infinity,
      url: `${host}/get_weather_realtime`,
      headers: { 'Content-Type': 'application/json' },
      data: data
    }
    const response = await axios.request(config)
    bp.logger.info(`Realtime response message:${JSON.stringify(response.data.message.toLowerCase())}`)

    if (response.data.message.toLowerCase() === 'ok') {
      event.state.session.locationData.locationTypo = false
      bp.logger.info(typeof response.data.content)
      event.state.session.weatherData = response.data.content
    } else {
      event.state.session.locationData.locationTypo = true
      // event.state.session.locationData.location = response.data.content.input_location
      event.state.session.locationData.inputLocation = response.data.content.input_location
      event.state.session.locationData.nearestLocation = response.data.content.nearest_location
    }
  } catch (error) {
    bp.logger.error('Requesting Realtime Weather Error: ', error)
  }
}

return requestRealtimeWeather(args.inputLocation)
