using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003649: Kupa
/// </summary>
public class _11003649 : NpcScript {
    internal _11003649(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009206$ 
                // - Eh heh heh. 
                return true;
            case 10:
                // $script:1109121007009207$ 
                // - And what brings a youngster like you here, hm? 
                switch (selection) {
                    // $script:1109121007009208$
                    // - I'm looking for someone.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009209$ 
                // - Looking for someone, eh? Well, you're in luck! I know everybody here. So, who is it you're after, hm? 
                switch (selection) {
                    // $script:1109121007009210$
                    // - Oh, I think I can find them on my own.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009211$ 
                // - Being tight-lipped about it, are you? $npcName:11003535[gender:1]$ trains her people well. 
                switch (selection) {
                    // $script:1109121007009212$
                    // - You're with Dark Wind?
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009213$ 
                // - Eh heh heh! Surprised? Even us old timers can help out sometimes. Anyway, you run along and tell her, "Eyes. Alpha. Blonde hair." 
                switch (selection) {
                    // $script:1109121007009214$
                    // - Will do!
                    case 0:
                        Id = 14;
                        return false;
                }
                return true;
            case 14:
                // $script:1109121007009215$ 
                // - Eh heh heh! 
                return true;
            default:
                return true;
        }
    }
}
