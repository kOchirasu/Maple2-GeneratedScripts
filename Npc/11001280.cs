using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001280: Eupheria
/// </summary>
public class _11001280 : NpcScript {
    internal _11001280(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1208234507004843$ 
                // - I-I'm not... strong enough...
                return true;
            case 30:
                // $script:1208234507004846$ 
                // - Gah! I failed to avenge Master Arazaad. Again!
                switch (selection) {
                    // $script:1208234507004847$
                    // - You'll get your chance.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1208234507004848$ 
                // - Just wait. Perhaps I'm not strong enough now, but I'll keep training. And someday, I'll rend $npcName:11001231[gender:0]$ asunder!
                return true;
            default:
                return true;
        }
    }
}
