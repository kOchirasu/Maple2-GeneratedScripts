using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001080: Yovo
/// </summary>
public class _11001080 : NpcScript {
    internal _11001080(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1216233107005208$ 
                // - The desert hides many secrets, and I'm going to uncover them all!
                return true;
            case 30:
                // $script:1216233107005211$ 
                // - You can feel it, too, can't you? There's something wrong here. You have sharp senses for a human.
                switch (selection) {
                    // $script:1216233107005212$
                    // - What is this strange energy?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1216233107005213$ 
                // - I wouldn't get too curious about it if I were you. In fact, keep your distance unless you have some good info for me. I don't have time to answer questions for ignoramuses.
                return true;
            default:
                return true;
        }
    }
}
