using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001140: Gadren
/// </summary>
public class _11001140 : NpcScript {
    internal _11001140(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911192907003908$ 
                // - What brings you to $map:02000110$?
                return true;
            case 30:
                // $script:0911192907003911$ 
                // - There's nothing more important than safety. Wouldn't you agree?
                switch (selection) {
                    // $script:0911192907003912$
                    // - I guess, sure.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0911192907003913$ 
                // - I know, right? But nobody else seems to get it! I see people come to work without their hard hats or work boots every day. Your goal should be to earn a living without killing yourself in the process!
                return true;
            default:
                return true;
        }
    }
}
