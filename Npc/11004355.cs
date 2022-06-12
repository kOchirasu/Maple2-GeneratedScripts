using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004355: Evelyn
/// </summary>
public class _11004355 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011765$
    // - Why can't we just have a normal celebration? This is ridiculous!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011766$
                // - This isn't... It's not at all what I wanted...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
