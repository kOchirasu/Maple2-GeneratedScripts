using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000358: Towe
/// </summary>
public class _11000358 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407001486$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407001488$
                // - I'm a new man. From now on, I'm going to live an honest life. I'm leaving my days of being a thug behind.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
