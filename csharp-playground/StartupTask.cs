// Copyright (c) Microsoft. All rights reserved.
//
// This is the sample Blinky Headless project for blinking LEDs on the
// Raspberry Pi using Windows 10 IoT Core.

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net.Http;
using Windows.ApplicationModel.Background;
using Windows.Devices.Gpio;
using Windows.System.Threading;

namespace BlinkyHeadlessCS
{
    public sealed class StartupTask : IBackgroundTask
    {
        BackgroundTaskDeferral deferral;

        private ThreadPoolTimer timer;

        public void Run(IBackgroundTaskInstance taskInstance)
        {
            deferral = taskInstance.GetDeferral();

            var stream = new FileStream(@"lol.mp3", FileMode.Open, FileAccess.Read).AsRandomAccessStream();
            var media = new System.Windows.Controls.MediaElement();
            media.AutoPlay = true;
            media.SetSource(stream, "audio/mpeg3");
            media.Volume = 0.9;
        }
    }
}
