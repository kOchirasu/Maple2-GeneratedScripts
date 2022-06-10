using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001122: Velte
/// </summary>
public class _11001122 : NpcScript {
    internal _11001122(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0910171307003829$ 
                // - Do you have business with me?
                return true;
            case 30:
                // $script:0910171307003832$ 
                // - Good day. My name is $npcName:11001122[gender:0]$, and I'm a member of the Wall Climbers. We're a group that supports each other as we work to climb every wall we can find. If you have a passion for climbing, we're right there with you!
                switch (selection) {
                    // $script:0910171307003833$
                    // - You look a little different from the other Wall Climbers.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0910171307003834$ 
                // - Really? How so? 
                switch (selection) {
                    // $script:0910171307003835$
                    // - Are you sure you're a Wall Climber?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0910171307003836$ 
                // - ...Sheesh, can't you just let it go? If you're going to keep asking stupid questions, I don't want to talk to you.
                return true;
            default:
                return true;
        }
    }
}
