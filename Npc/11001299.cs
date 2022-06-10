using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001299: Allon
/// </summary>
public class _11001299 : NpcScript {
    internal _11001299(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005013$ 
                // - How may I help you? 
                return true;
            case 10:
                // $script:1228222807005744$ 
                // - Remember what the empress told you! 
                return true;
            default:
                return true;
        }
    }
}
