import subprocess
import os
import shutil

# Пътища към локалните директории на репозиториите
source_repo_path = r"C:\Users\a1bg537940\Desktop\linkove"
destination_repo_path = r"C:\Users\a1bg537940\Desktop\General"

# Файлът, който ще бъде копиран и модифициран
file_to_copy = 'video_stream.m3u'

# Функция за изпълнение на git команди
def run_git_command(command, repo_path):
    try:
        result = subprocess.run(command, cwd=repo_path, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running command {command} in {repo_path}: {e}")
        print(e.stderr)

# Стъпка 1: Актуализиране на source репозиториото
def update_repo(repo_path):
    print(f"Updating repository in {repo_path}...")
    run_git_command(['git', 'pull'], repo_path)

# Стъпка 2: Копиране на файла от source репозиториото към destination репозиториото
def copy_file_to_destination():
    print(f"Copying {file_to_copy} from source to destination...")
    source_file_path = os.path.join(source_repo_path, file_to_copy)
    destination_file_path = os.path.join(destination_repo_path, file_to_copy)
    
    if os.path.exists(source_file_path):
        shutil.copy2(source_file_path, destination_file_path)
        print(f"File copied to {destination_file_path}")
    else:
        print(f"{file_to_copy} not found in {source_repo_path}.")

# Стъпка 3: Редактиране на съдържанието на файла в destination репозиториото
def edit_file_in_destination():
    destination_file_path = os.path.join(destination_repo_path, file_to_copy)
    try:
        with open(destination_file_path, 'r+', encoding='utf-8') as file:
            content = file.read()
            # Заменяме 'BNT' с 'neBNT' и 'btv' с 'neBTV'
            content = content.replace('#EXTM3U', '#EXTM3U catchup="flussonic" url-tvg="https://github.com/harrygg/EPG/raw/refs/heads/master/all-2days.details.epg.xml.gz"').replace('#EXTINF:-1,BNT1', '#EXTINF:-1 tvg-name="BNT 1" tvg-logo="https://www.glebul.com/images/tv-logo/bnt-1-hd.png" group-title="ЕФИРНИ" , BNT 1 HD').replace('#EXTINF:-1,BNT2', '#EXTINF:-1 tvg-name="BNT 2" tvg-logo="https://www.glebul.com/images/tv-logo/bnt-2.png" group-title="ЕФИРНИ" , BNT 2').replace('#EXTINF:-1,BNT3', '#EXTINF:-1 tvg-name="BNT 3" tvg-logo="https://www.glebul.com/images/tv-logo/bnt-3-hd.png" group-title="ЕФИРНИ" , BNT 3').replace('#EXTINF:-1,BNT4', '#EXTINF:-1 tvg-name="BNT 4" tvg-logo="https://www.glebul.com/images/tv-logo/bnt-4.png" group-title="ЕФИРНИ" , BNT 4 HD').replace('#EXTINF:-1,Nova', '#EXTINF:-1 tvg-name="Nova TV" tvg-logo="https://www.glebul.com/images/tv-logo/nova-tv-hd.png" group-title="ЕФИРНИ" , NovaTV').replace('#EXTINF:-1,bTV', '#EXTINF:-1 tvg-name="bTV" tvg-logo="https://www.glebul.com/images/tv-logo/btv-hd.png" group-title="ЕФИРНИ" , bTV HD').replace('#EXTINF:-1,bTVAction', '#EXTINF:-1 tvg-name="bTV Action" tvg-logo="https://www.glebul.com/images/tv-logo/btv-action-hd.png" group-title="Спортни"  , bTV Action HD').replace('#EXTINF:-1,bTVCinema', '#EXTINF:-1 tvg-name="bTV Cinema" tvg-logo="https://www.glebul.com/images/tv-logo/btv-cinema.png" group-title="Филмови" , bTV Cinema HD').replace('#EXTINF:-1,bTVComedy', '#EXTINF:-1 tvg-name="bTV Comedy" tvg-logo="https://www.glebul.com/images/tv-logo/btv-comedy.png" group-title="Филмови" , bTV Comedy HD').replace('#EXTINF:-1,bTVStory', '#EXTINF:-1 tvg-name="bTV Story" tvg-logo="https://www.glebul.com/images/tv-logo/btv-story.png" group-title="Филмови" , bTV Story HD').replace('#EXTINF:-1,KinoNova', '#EXTINF:-1 tvg-name="KinoNova" tvg-logo="https://www.glebul.com/images/tv-logo/kino-nova.png" group-title="Филмови" , KinoNova').replace('#EXTINF:-1,Diema', '#EXTINF:-1 tvg-name="Diema" tvg-logo="https://www.glebul.com/images/tv-logo/diema.png" group-title="Филмови" , Diema ').replace('#EXTINF:-1,DiemaFamily', '#EXTINF:-1 tvg-name="Diema Family" tvg-logo="https://www.glebul.com/images/tv-logo/diema-family.png" group-title="Филмови" , Diema Family').replace('#EXTINF:-1,STARChannel', '#EXTINF:-1 tvg-name="STAR CHANNEL" tvg-logo="https://www.glebul.com/images/tv-logo/star-channel-hd.png" group-title="Филмови" , STAR CHANNEL HD').replace('#EXTINF:-1,STARLife', '#EXTINF:-1 tvg-name="STAR Life" tvg-logo="https://www.glebul.com/images/tv-logo/star-life-hd.png" group-title="Филмови" , STAR Life HD').replace('#EXTINF:-1,STARCrime', '#EXTINF:-1 tvg-name="STAR Crime " tvg-logo="https://www.glebul.com/images/tv-logo/star-crime-hd.png" group-title="Филмови" , STAR Crime HD').replace('#EXTINF:-1,FilmBoxStars', '#EXTINF:-1 tvg-id="FilmboxStars.bg" tvg-name="BG:FilmBox Stars HD" tvg-logo="http://iphd.tv/service/bulsat/filmbox_stars-18-02-2021.svg" group-title="Филмови" , FilmBox Stars HD').replace('#EXTINF:-1,FilmBoXtraHD', '#EXTINF:-1 tvg-id="FilmBoxExtra.bg" tvg-name="BG:FilmBox Extra HD" tvg-logo="http://iphd.tv/service/bulsat/filmbox_extra-16-02-2021.svg" group-title="Филмови" , FilmBox Extra HD').replace('#EXTINF:-1,MovieStar', '#EXTINF:-1 tvg-id="MovieStar.bg" tvg-name="BG:Moviestar HD" tvg-logo="http://iphd.tv/service/bulsat/moviestar-23-04-2019.svg" group-title="Филмови" , Moviestar HD').replace('#EXTINF:-1,AMC', '#EXTINF:-1 tvg-id="AMC.bg" tvg-name="BG:AMC" tvg-logo="http://iphd.tv/service/bulsat/amc-17-02-2022.svg" group-title="Филмови" , AMC').replace('#EXTINF:-1,AXN', '#EXTINF:-1 tvg-id="AXN.bg" tvg-name="BG:AXN" tvg-logo="http://iphd.tv/service/bulsat/axn-23-04-2019.svg" group-title="Филмови" , AXN').replace('#EXTINF:-1,24kitchen', '#EXTINF:-1 tvg-name="24 Kitchen" tvg-logo="https://www.glebul.com/images/tv-logo/24-kitchen-hd.png" group-title="Други" , 24 Kitchen HD').replace('#EXTINF:-1,Discovery', '#EXTINF:-1 tvg-name="Discovery Channel" tvg-logo="https://www.glebul.com/images/tv-logo/discovery-channel-hd.png" group-title="Научни" , Discovery Channel HD').replace('#EXTINF:-1,NatGeo', '#EXTINF:-1 tvg-name="National Geographic" tvg-logo="https://www.glebul.com/images/tv-logo/nat-geo-hd.png" group-title="Научни" , National Geographic HD').replace('#EXTINF:-1,NatGeoWild', '#EXTINF:-1 tvg-name="Nat Geo Wild" tvg-logo="https://www.glebul.com/images/tv-logo/nat-geo-wild-hd.png" group-title="Научни" , Nat Geo Wild HD').replace('#EXTINF:-1,History', '#EXTINF:-1 tvg-id="HistoryChannel.bg" tvg-name="BG:History Channel HD" tvg-logo="http://iphd.tv/service/bulsat/history_channel-23-04-2019.svg" group-title="Научни" , History Channel HD').replace('#EXTINF:-1,Docubox', '#EXTINF:-1 tvg-id="DocuBox.bg" tvg-name="BG:Docu Box HD" tvg-logo="http://iphd.tv/service/bulsat/docubox-16-02-2021.svg" group-title="Научни" , Docu Box HD').replace('#EXTINF:-1,ViasatExplorer', '#EXTINF:-1 tvg-id="ViasatExplorer.bg" tvg-name="BG:Viasat Explore HD" tvg-logo="http://iphd.tv/service/bulsat/viasat_explore-17-02-2022.svg" group-title="Научни" , Viasat Explore HD').replace('#EXTINF:-1,ViasatHistory', '#EXTINF:-1 tvg-id="ViasatHistory.bg" tvg-name="BG:Viasat History HD" tvg-logo="http://iphd.tv/service/bulsat/viasat_history-17-02-2022.svg" group-title="Научни" , Viasat History HD').replace('#EXTINF:-1,ViasatNature', '#EXTINF:-1 tvg-id="ViasatNature.bg" tvg-name="BG:Viasat Nature HD" tvg-logo="http://iphd.tv/service/bulsat/viasat_nature-17-02-2022.svg" group-title="Научни" , Viasat Nature HD').replace('#EXTINF:-1,AnimalPlanet', '#EXTINF:-1 tvg-id="AnimalPlanet.bg" tvg-name="BG:Animal Planet HD" tvg-logo="http://iphd.tv/service/bulsat/animal_planet-23-04-2019.svg" group-title="Научни" , Animal Planet HD').replace('#EXTINF:-1,TLC', '#EXTINF:-1 tvg-name="TLC" tvg-logo="https://www.glebul.com/images/tv-logo/tlc.png" group-title="Други" , TLC HD').replace('#EXTINF:-1,Balkanika', '#EXTINF:-1 tvg-id="Balkanika.bg" tvg-name="BG:Balkanika HD" tvg-logo="http://iphd.tv/service/bulsat/balkanika-23-04-2019.svg" group-title="Музикални" , Balkanika HD').replace('#EXTINF:-1,Planeta', '#EXTINF:-1 tvg-name="Planeta HD" tvg-logo="https://www.glebul.com/images/tv-logo/planeta-hd.png" group-title="Музикални" , Planeta HD').replace('#EXTINF:-1,PlanetaFolk', '#EXTINF:-1 tvg-name="Planeta Folk" tvg-logo="https://www.glebul.com/images/tv-logo/planeta-folk.png" group-title="Музикални" , Planeta Folk').replace('#EXTINF:-1,DiemaSport', '#EXTINF:-1 tvg-name="Diema Sport" tvg-logo="https://www.glebul.com/images/tv-logo/diema-sport-hd.png" group-title="Спортни" , Diema Sport').replace('#EXTINF:-1,DiemaSport2', '#EXTINF:-1 tvg-name="Diema Sport 2" tvg-logo="https://www.glebul.com/images/tv-logo/diema-sport-2-hd.png" group-title="Спортни" , Diema Sport 2').replace('#EXTINF:-1,DiemaSport3', '#EXTINF:-1 tvg-name="Diema Sport 3" tvg-logo="https://www.glebul.com/images/tv-logo/diema-sport-3-hd.png" group-title="Спортни" , Diema Sport 3').replace('#EXTINF:-1,MAXSport1', '#EXTINF:-1 tvg-name="Max Sport 1 HD" tvg-logo="https://www.glebul.com/images/tv-logo/max-sport-1-hd.png" group-title="Спортни" , Max Sport 1 HD').replace('#EXTINF:-1,MAXSport2', '#EXTINF:-1 tvg-name="Max Sport 2 HD" tvg-logo="https://www.glebul.com/images/tv-logo/max-sport-2-hd.png" group-title="Спортни" , Max Sport 2 HD').replace('#EXTINF:-1,MAXSport3', '#EXTINF:-1 tvg-name="Max Sport 3 HD" tvg-logo="https://www.glebul.com/images/tv-logo/max-sport-3-hd.png" group-title="Спортни" , Max Sport 3 HD').replace('#EXTINF:-1,MAXSport4', '#EXTINF:-1 tvg-name="Max Sport 4 HD" tvg-logo="https://www.glebul.com/images/tv-logo/max-sport-4-hd.png" group-title="Спортни" , Max Sport 4 HD').replace('#EXTINF:-1,NovaSport', '#EXTINF:-1 tvg-name="Nova Sport" tvg-logo="https://www.glebul.com/images/tv-logo/nova-sport-hd.png" group-title="Спортни" , Nova Sport HD').replace('#EXTINF:-1,RING', '#EXTINF:-1 tvg-name="Ring BG" tvg-logo="https://www.glebul.com/images/tv-logo/ring-bg-hd.png" group-title="Спортни" , Ring BG')
            # Изтриваме последните 16 реда
            lines = content.splitlines()
            if len(lines) > 16:
                content = '\n'.join(lines[:-16])
            file.seek(0)
            file.truncate()
            file.write(content)
        print(f"File {file_to_copy} edited successfully in {destination_repo_path}")
    except Exception as e:
        print(f"Error editing the file {file_to_copy} in {destination_repo_path}: {e}")

# Стъпка 4: Commit и push в destination репозиториото
def commit_and_push_changes():
    print("Committing and pushing changes to the destination repository...")
    run_git_command(['git', 'add', '.'], destination_repo_path)
    run_git_command(['git', 'commit', '-m', 'Updated file with new content'], destination_repo_path)
    run_git_command(['git', 'push'], destination_repo_path)

# Основен процес
def main():
    # Актуализираме и двете репозитории преди всяка друга стъпка
    update_repo(source_repo_path)
    update_repo(destination_repo_path)
    
    # Копираме файла от source към destination
    copy_file_to_destination()
    
    # Редактираме файла в destination репозиториото
    edit_file_in_destination()
    
    # Правим commit и push в destination репозиториото
    commit_and_push_changes()

if __name__ == "__main__":
    main()
