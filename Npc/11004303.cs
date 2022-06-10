using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004303: Ghost
/// </summary>
public class _11004303 : NpcScript {
    internal _11004303(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1002141907011426$ 
                // - This place is nice...
                return true;
            case 30:
                // $script:1002141907011429$ 
                // - This room's really comfy. That's why all us ghosts are here. 
                // $script:1002141907011430$ 
                // - We don't wanna bug the living folks, though. We just wanna watch them live their lives.
                switch (selection) {
                    // $script:1002141907011431$
                    // - Did you see what happened here?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1002141907011432$ 
                // - I-I was scared, so I hid behind the chair! That guy was real busy. I bet he dropped a bunch of his stuff all over the place.
                return true;
            default:
                return true;
        }
    }
}
