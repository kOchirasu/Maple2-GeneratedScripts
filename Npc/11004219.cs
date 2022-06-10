using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004219: Rekk
/// </summary>
public class _11004219 : NpcScript {
    internal _11004219(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806222707010782$ 
                // - Was there something you needed?
                return true;
            case 10:
                // $script:0806222707010783$ 
                // - There is power in anger, but you must never lose yourself in the heat of battle. When all that's left is devastation, there are no winners.
                return true;
            default:
                return true;
        }
    }
}
