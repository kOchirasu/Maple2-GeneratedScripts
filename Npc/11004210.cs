using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004210: Ruru
/// </summary>
public class _11004210 : NpcScript {
    internal _11004210(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806045807010666$ 
                // - Yaaaaaawn...
                return true;
            case 10:
                // $script:0806045807010667$ 
                // - You want to try out some high-caliber mushsplosives? Just pick up a bomb and throw it.
                switch (selection) {
                    // $script:0806052007010672$
                    // - Right... And how do I pick stuff up again?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0806052107010672$ 
                // - You don't know? Just stand next to a bomb and the words "Pick Up" will pop up in the air as if by magic. Just press the corresponding button and you're ready to unleash the cleansing power of fire!
                switch (selection) {
                    // $script:0806052107010673$
                    // - ...None of that seems strange to you?
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0806052107010674$ 
                // - No stranger than the voices in my head that tell me to burn things!
                return true;
            default:
                return true;
        }
    }
}
