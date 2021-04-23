function track = wavePlot(trackName,path,sf)
    trackName = string(trackName);
    path = string(path);
    
    if ~ endsWith(trackName,".csv")
        trackName = trackName+".csv";
    elseif ~ endsWith(path,"/")
        path = path+"/";
    end

    track = csvread(path+trackName)';
    
    time = 1:length(track);
    
    figure()
    plot(time/sf,track);
    xlabel('Time [s]')
    ylabel('Amplitude')
    title('Waveplot of '+ trackName)
    grid on; axis tight;
    pbaspect([64 9 1]);

