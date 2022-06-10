using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004173: Tara
/// </summary>
public class _11004173 : NpcScript {
    internal _11004173(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010608$ 
                // - Mm?
                return true;
            case 10:
                // $script:0806025707010609$ 
                // - Sorry, I've already got a squad. See? There's the guy selling churros, the girl strutting around over there, and that guy shooting finger-guns.  I couldn't ask for better teammates.
                return true;
            default:
                return true;
        }
    }
}
