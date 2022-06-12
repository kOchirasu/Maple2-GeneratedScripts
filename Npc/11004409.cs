using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004409: Condor
/// </summary>
public class _11004409 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1113161307011835$
    // - Back in my day, we knew a thing or two about duty!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1113161307011836$
                // - Flying continents appearing from nowhere? Ha! This is nothing. You should've seen the crazy things that happened back in <i>my</i> day!
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
