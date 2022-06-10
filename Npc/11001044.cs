using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001044: Papa Santa
/// </summary>
public class _11001044 : NpcScript {
    internal _11001044(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003565$ 
                // - I'm the messenger of hopes and dreams! Why is this happening to me?  
                return true;
            case 30:
                // $script:0831180407003568$ 
                // - I like being a Santa. How could I not? I'm giving people joy! 
                return true;
            default:
                return true;
        }
    }
}
