  /**
   * send Weather Data to chat
   * @title sendWeatherData
   * @category InteractiveChat
   * @author Ahmad
   */
  const sendWeatherData = async () => {
    try {
      bp.logger.info(JSON.stringify(event.state.session.weatherData, null, 2))
      bp.logger.info(event.state.session.weatherData.length)
      const message = {
        type: 'text',
        text: JSON.stringify(event.state.session.weatherData, null, 2)
      }

      bp.events.replyToEvent(event, [message])
    } catch (error) {
      bp.logger.error(error)
    }
  }

  return sendWeatherData()
