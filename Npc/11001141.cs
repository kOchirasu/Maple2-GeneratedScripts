using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001141: Melvo
/// </summary>
public class _11001141 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0914192507003916$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0914192507003919$
                // - Hello, and welcome to the Andrea Family estate. As its caretaker I would love to give you a tour, but I'm afraid I have some eggs to collect.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
