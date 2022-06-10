using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000995: Maruchi
/// </summary>
public class _11000995 : NpcScript {
    internal _11000995(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003416$ 
                // - Ah, what is it?
                return true;
            case 30:
                // $script:0831180407003419$ 
                // - Some people say I don't look like an adventurer. They think I would look more relaxed sitting behind a desk, reading and daydreaming.
                // $script:0831180407003420$ 
                // - That means they don't know me. I prefer seeing things for myself rather than reading them from books. That's why I'm so happy about this job with the Adventurer's Guild.
                return true;
            default:
                return true;
        }
    }
}
