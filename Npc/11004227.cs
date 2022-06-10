using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004227: Roca
/// </summary>
public class _11004227 : NpcScript {
    internal _11004227(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806222707010804$ 
                // - Hello.
                return true;
            case 10:
                // $script:0806222707010805$ 
                // - Sigh... I can't go in there without my squad, but my friends are all no-shows and I'm starting to get pretty bored.
                return true;
            default:
                return true;
        }
    }
}
