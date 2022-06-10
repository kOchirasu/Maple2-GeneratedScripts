using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000280: Ted
/// </summary>
public class _11000280 : NpcScript {
    internal _11000280(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001090$ 
                // - What seems to be the problem? 
                return true;
            case 30:
                // $script:0831180407001093$ 
                // - A castle once stood on this very spot, the ancestral home of the Andreas. They were a noble family with close ties to the royals dating back generations. Then one day... the castle simply vanished. 
                // $script:0831180407001094$ 
                // - That guy does nothing but read books all day. He's supposed to be investigating the scene. 
                return true;
            default:
                return true;
        }
    }
}
