using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000178: Mrs. Ibelin
/// </summary>
public class _11000178 : NpcScript {
    internal _11000178(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000734$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407000737$ 
                // - My son is doing very important work at $map:02000001$ Palace. I couldn't provide for him when he was young, but he still grew into such a great man. I'm so proud of him. 
                return true;
            default:
                return true;
        }
    }
}
