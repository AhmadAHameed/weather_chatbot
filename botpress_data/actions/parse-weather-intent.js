const axios = require('axios')
const { host } = require('./shared')
/**
 * Parse intent to handle weather request
 * @title WeatherIntentParser
 * @category Parsers
 * @author Ahmad
 * @param {string} inputMessage - An example string variable
 */
const mainIntentParser = async inputMessage => {
  try {
    const data = JSON.stringify({ message: inputMessage })
    const config = {
      method: 'post',
      maxBodyLength: Infinity,
      url: `${host}/nlu/parse`,
      headers: { 'Content-Type': 'application/json' },
      data: data
    }
    const response = await axios.request(config)

    let entities = []
    const intentThreshold = 0.7
    const entityThreshold = 0.7
    event.nlu.intent.name = ''
    event.state.session.entities = ''

    if (response.status === 200) {
      if (response.data.result.intent.confidence >= intentThreshold) {
        bp.logger.info(JSON.stringify(response.data.result.intent.name))
        event.nlu.intent.name = response.data.result.intent.name
      } else {
        bp.logger.info("WeatherIntent couldn't be recognised!!")
        return
      }
      response.data.result.entities.forEach(entity => {
        if (entity.confidence_entity >= entityThreshold) {
          entities.push(entity)
        }
      })
      if (entities.length > 0) {
        // Only consider [entity, value & confidence_entity] keys
        entities = entities.map(({ entity, value, confidence_entity }) => ({
          entity,
          value,
          confidence_entity
        }))
        event.state.session.entities = entities
      }
    }
  } catch (error) {
    bp.logger.error(error)
  }
}

return mainIntentParser(args.inputMessage)
