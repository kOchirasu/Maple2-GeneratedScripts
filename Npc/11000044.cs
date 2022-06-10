using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000044: Katvan
/// </summary>
public class _11000044 : NpcScript {
    internal _11000044(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000209$ 
                // - Let's get to business. 
                return true;
            case 30:
                // $script:0831180407000212$ 
                // - I'll admit, not everyone in Dark Wind was happy when I took over. Many were loyal to Captain Winn, not the organization. After he passed away, $npcName:11000006[gender:0]$ took some of our best agents and left. 
                // $script:0831180407000213$ 
                // - But I have my own principles to follow and I intend to lead Dark Wind in my own way. Winn Stilton was a great man, but we won't live in his shadow. 
                // $script:0831180407000214$ 
                // - The others may not be on board yet, but they'll come around. Eventually. 
                return true;
            default:
                return true;
        }
    }
}
