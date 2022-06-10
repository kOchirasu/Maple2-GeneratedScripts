using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003163: Nelph
/// </summary>
public class _11003163 : NpcScript {
    internal _11003163(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0310134607008074$ 
                // - Welcome to the $map:52000116$. I am $npcName:11003163[gender:0]$. If you have any questions regarding the caravans, feel free to ask.
                return true;
            case 30:
                // $script:0310134607008077$ 
                // - My job is to make sure $npcName:11000075[gender:1]$ and the other members of the royal family have everything they desire. I'm always busy, but I take pride in my position and my service to $map:02000025$.
                return true;
            case 31:
                // $script:0310134607008078$ 
                // - These matters are not normally my responsibility, of course, but $npcName:11003165[gender:0]$ asked for me personally due to the... sensitive nature.
                return true;
            case 40:
                // $script:0310134607008079$ 
                // - Have you been to $map:02000076$? My mother lives there. I really should visit her, but I've been so busy that I haven't had the time since preparations began. 
                return true;
            case 41:
                // $script:0310134607008080$ 
                // - Once my work here is done, I'll go and visit her first thing! I've been sending her letters, it's just... she can't see. A disease took her eyesight. Sigh... 
                return true;
            default:
                return true;
        }
    }
}
