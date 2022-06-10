using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004152: Tina
/// </summary>
public class _11004152 : NpcScript {
    internal _11004152(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010575$ 
                // - Can I help you? 
                return true;
            case 10:
                // $script:0806025707010576$ 
                // - The scenery here is breathtaking, but if you want the best view in $map:02000499$, you should try hanging from $npcName:11004165$. 
                return true;
            default:
                return true;
        }
    }
}
