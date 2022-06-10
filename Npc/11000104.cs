using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000104: Santiago
/// </summary>
public class _11000104 : NpcScript {
    internal _11000104(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000425$ 
                // - Hey there! 
                return true;
            case 30:
                // $script:0831180407000428$ 
                // - Well aren't you a sight for sore eyes. It's been a while since I've seen anybody that wasn't a skeleton or an angry octo-thing looking to bludgeon me to death. 
                return true;
            default:
                return true;
        }
    }
}
