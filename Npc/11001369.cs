using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001369: Livet
/// </summary>
public class _11001369 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1110153306000979$
    // - Hello, hello, hello! I'm <i>triple</i> happy to see you! 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1110153306000982$
                // - Amazing that such a glorious city can thrive here, don't you think?
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
