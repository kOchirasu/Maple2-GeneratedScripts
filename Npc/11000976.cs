using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000976: Jinbar
/// </summary>
public class _11000976 : NpcScript {
    internal _11000976(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003376$ 
                // - Wa-tcha! Hyoo! <i>That</i> is the sound of a master martial artist! 
                return true;
            case 20:
                // $script:0831180407003378$ 
                // - Nothing is impossible for true martial artists. Do you want to become strong? It won't be easy.  
                return true;
            default:
                return true;
        }
    }
}
