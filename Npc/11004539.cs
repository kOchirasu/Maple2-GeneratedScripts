using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004539: Barricade Defender
/// </summary>
public class _11004539 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0104170807012621$
    // - Ah! You startled me!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0104170807012622$
                // - Ah! You startled me!
                return 10;
            case (10, 1):
                // $script:0104170807012623$
                // - You better watch out who you sneak up on. I was two seconds away from tombstoning you!
                return 10;
            case (10, 2):
                // $script:0104170807012624$
                // - If you have time to chat, you have time to fight!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
