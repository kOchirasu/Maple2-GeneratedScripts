using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000147: Benhurst
/// </summary>
public class _11000147 : NpcScript {
    internal _11000147(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000628$ 
                // - What is it?
                return true;
            case 20:
                // $script:0831180407000630$ 
                // - When will I ever have another chance to see the empress in person? I really want to go see the court!
                return true;
            default:
                return true;
        }
    }
}
