using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000385: Shalin
/// </summary>
public class _11000385 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001568$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001570$
                // - If you see trash on the street, by all means pick it up! Everyone has to do their part to keep their homes clean.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
