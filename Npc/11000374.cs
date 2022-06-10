using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000374: Tann
/// </summary>
public class _11000374 : NpcScript {
    internal _11000374(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001534$ 
                // - What?
                return true;
            case 30:
                // $script:0831180407001537$ 
                // - What?
                switch (selection) {
                    // $script:0831180407001538$
                    // - So uh... are you a dude or a lady?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407001539$ 
                // - Think what you like!
                return true;
            case 60:
                // $script:0831180407001540$ 
                // - There are treasure chests hidden all over the world. How did they get there? Who knows and who cares! Just remember the golden rule: finders keepers!
                return true;
            default:
                return true;
        }
    }
}
