using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000995: Maruchi
/// </summary>
public class _11000995 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003416$
    // - Ah, what is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003419$
                // - Some people say I don't look like an adventurer. They think I would look more relaxed sitting behind a desk, reading and daydreaming.
                return 30;
            case (30, 1):
                // $script:0831180407003420$
                // - That means they don't know me. I prefer seeing things for myself rather than reading them from books. That's why I'm so happy about this job with the Adventurer's Guild.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
